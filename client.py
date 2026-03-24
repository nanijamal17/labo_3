import asyncio
import cv2
from aiortc import RTCPeerConnection
from aiortc.contrib.signaling import TcpSocketSignaling, BYE


class VideoReceiver:
    def __init__(self):
        self.track = None

    async def receive_track(self, track):
        self.track = track

        while True:
            frame = await asyncio.wait_for(self.track.recv(), timeout=30.0)

            # Conversion de la frame WebRTC en image exploitable par OpenCV
            image = frame.to_ndarray(format="bgr24")

            # Affichage de la vidéo
            cv2.imshow("Flux video recu", image)

            # Touche q pour quitter
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cv2.destroyAllWindows()


async def stream(connection, signaling, video_receiver):
    await signaling.connect()

    @connection.on("track")
    def on_track(track):
        video_receiver.track = track
        asyncio.create_task(video_receiver.receive_track(track))

    # Négociation des paramètres de connexion
    offer = await connection.createOffer()
    await connection.setLocalDescription(offer)
    await signaling.send(connection.localDescription)

    answer = await signaling.receive()
    await connection.setRemoteDescription(answer)

    print("Connexion établie, réception du flux vidéo...")

    while True:
        await asyncio.sleep(1)


async def main():
    server_ip = "127.0.0.1"
    server_port = 9999

    signaling = TcpSocketSignaling(server_ip, server_port)
    connection = RTCPeerConnection()
    video_receiver = VideoReceiver()

    await stream(connection, signaling, video_receiver)


if __name__ == "__main__":
    asyncio.run(main())