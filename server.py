from aiortc import VideoStreamTrack
import cv2

class WebcamVideoStreamTrack(VideoStreamTrack):
    #Surcharge du constructeur
    def __init__(self, camera_id):
        super().__init__()
        self.web_cam = cv2.VideoCapture(camera_id)
        ...

    async def recv(self):
        #Ajouter ici la logique pour récupérer et traiter une trame vidéo puis retournez la trame vidéo capturée.
        # Récupérer l'horodatage WebRTC
        pts, time_base = await self.next_timestamp()

        # Lire une trame depuis la webcam
        ret, frame = self.web_cam.read()
        if not ret:
            raise Exception("Impossible de lire la webcam")

        # Convertir l'image OpenCV en frame vidéo WebRTC
        video_frame = VideoFrame.from_ndarray(frame, format="bgr24")
        video_frame.pts = pts
        video_frame.time_base = time_base

        return video_frame

    async def setup_and_run_server(server_ip, server_port, webcam_id):
        signaling = TcpSocketSignaling(server_ip, server_port)
        connection = RTCPeerConnection()
        video_streamer = WebcamVideoStreamTrack(webcam_id)

        # Ajouter le flux vidéo à la connexion
        connection.addTrack(video_streamer)

        # Connexion au canal de signalisation
        await signaling.connect()
        print("Serveur prêt, en attente d'un client...")

        # Négociation des paramètres
        offer = await signaling.receive()
        await connection.setRemoteDescription(offer)

        answer = await connection.createAnswer()
        await connection.setLocalDescription(answer)
        await signaling.send(connection.localDescription)

        print("Connexion établie, début du streaming...")

        # Boucle infinie jusqu'à interruption
        while True:
            obj = await signaling.receive()
            if obj is BYE:
                print("Communication interrompue.")
                break

    async def main():
        ip_address = "127.0.0.1"
        port = 9999
        camera_id = 0

        await setup_and_run_server(ip_address, port, camera_id)

    asyncio.run(main())