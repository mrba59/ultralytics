import { Alpine } from "../libs/alpine.esm.js";

const VideoStuff = {
    videoRef: /** @type {HTMLVideoElement} */ (document.querySelector("#video-player")),
    canvasRef: /** @type {HTMLCanvasElement} */ (document.querySelector("#video-canvas")),
    videoMetaData: {
        width: 3840,
        heigth: 2160,
        fps: 5,
    },
    /** @type {Array<any>} */
    videoFramesInfo: Alpine.$persist([]),
    currentFrame: 1,
    isVideoPlaying: false,
    loopIntervalId: 0,

    removeIdFromDataSet(id) {
        for (let i = this.currentFrame - 1; i < this.videoFramesInfo.length; i++) {
            this.videoFramesInfo[i].elements = this.videoFramesInfo[i].elements.filter(
                (e) => e.elementId != id
            );
        }
        this.drawToCanvas();
    },
    changeIdOfElement(oldId, newId) {
        for (let i = this.currentFrame - 1; i < this.videoFramesInfo.length; i++) {
            this.videoFramesInfo[i].elements.forEach((e) => {
                if (e.elementId == oldId) {
                    e.elementId = Number(newId);
                }
            });
        }
        this.drawToCanvas();
    },

    getFrameData() {
        if (!this.videoFramesInfo.length) return [];
        return this.videoFramesInfo[this.currentFrame - 1].elements;
    },
    nextFrame() {
        this.currentFrame++;
        this.drawToCanvas();

        if (!this.isVideoPlaying) {
            this.setVideoFrame();
        }
    },
    prevFrame() {
        if (this.currentFrame > 1) {
            this.currentFrame--;
            this.drawToCanvas();

            if (!this.isVideoPlaying) {
                this.setVideoFrame();
            }
        }
    },
    pause() {
        this.setVideoFrame();

        if (this.isVideoPlaying) {
            this.isVideoPlaying = false;
            this.videoRef.pause();
            clearInterval(this.loopIntervalId);
            this.loopIntervalId = 0;
            return;
        }

        this.isVideoPlaying = true;
        this.videoRef.play();

        this.loopIntervalId = setInterval(() => {
            this.nextFrame();
        }, 1000 / this.videoMetaData.fps);
    },
    setVideoFrame() {
        this.videoRef.currentTime = this.currentFrame / this.videoMetaData.fps;
    },

    drawToCanvas() {
        const WIDTH = this.canvasRef.width;
        const HEIGTH = this.canvasRef.height;

        const ctx = this.canvasRef.getContext("2d");
        if (!ctx) return;

        //clear canvas to redraw everything
        ctx.clearRect(0, 0, WIDTH, HEIGTH);

        ctx.font = "20px Arial";
        ctx.lineWidth = 0.5;
        ctx.strokeStyle = "red";
        ctx.fillStyle = "black";

        for (let element of this.videoFramesInfo[this.currentFrame - 1].elements) {
            const { x, y, h, w, elementId } = element;

            //assuming x and y are center points ?
            const X = x * WIDTH - (w * WIDTH) / 2;
            const Y = y * HEIGTH - (h * HEIGTH) / 2;

            ctx.strokeRect(X, Y, w * WIDTH, h * HEIGTH);
            ctx.fillText(elementId, X, Y - 2);
        }
    },

    async getVideo(project = "tetegehm_malo") {
        const res = await fetch("assets/" + project + ".json");
        const data = await res.json();

        //this.videoFramesInfo = data;
        this.videoRef.src = "assets/" + project + ".mp4";

        this.drawToCanvas();
    },

    setDimensions() {
        const container = /** @type {HTMLDivElement} */ (
            document.querySelector("#video-container")
        );

        this.canvasRef.width = container.offsetWidth;
        this.canvasRef.height = container.offsetHeight;

        this.videoRef.width = container.offsetWidth;
        this.videoRef.height = container.offsetHeight;
    },

    init() {
        if (this._isIinit) return;
        this._isIinit = true;

        this.setDimensions();
        this.getVideo();
    },
    _isIinit: false,
};

export default VideoStuff;
