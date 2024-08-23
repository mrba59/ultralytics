import {Alpine} from "../libs/alpine.esm.js";

const videoRef = /** @type {HTMLVideoElement} */ (document.querySelector("#video-player"))

const canvasRef = /** @type {HTMLCanvasElement} */ (document.querySelector("#video-canvas"))
const ctx = canvasRef.getContext("2d");


const VideoStuff = {
    videoMetaData: Alpine.$persist({}),
    videoPath: Alpine.$persist(""),
    /** @type {Array<any>} */
    videoFramesInfo: Alpine.$persist([]),
    currentFrame: 0,
    isVideoPlaying: false,

    removeIdFromDataSet(id) {
        for (let i = this.getVideoFrame(); i < this.videoFramesInfo.length; i++) {
            this.videoFramesInfo[i].elements = this.videoFramesInfo[i].elements.filter(
                (e) => e.elementId != id
            );
        }
    },

    changeIdOfElement(oldId, newId) {
        for (let i = this.getVideoFrame(); i < this.videoFramesInfo.length; i++) {
            this.videoFramesInfo[i].elements.forEach((e) => {
                if (e.elementId == oldId) {
                    e.elementId = Number(newId);
                }
            });
        }
    },
    
    getFrameData() {
        if (!this.videoFramesInfo.length) return [];
        return this.videoFramesInfo[this.currentFrame].elements;
    },

    nextFrame() {
        if (this.getVideoFrame() == this.videoFramesInfo.length) return    
        videoRef.currentTime += 1/(30/3)
    },

    prevFrame() {
        if (this.getVideoFrame() < 1) return
        videoRef.currentTime -= 1/(30/3)
    },

    pause() {
        if (this.isVideoPlaying) {
            videoRef.pause();
            this.isVideoPlaying = false
        } else {
            videoRef.play();
            this.isVideoPlaying = true
        }
        setTimeout(()=>this.setDimensions(),10)
    },

    setVideoFrame() {
        videoRef.currentTime = this.currentFrame / (30/3);
    },

    getVideoFrame(){
        return Math.floor(videoRef.currentTime*(30/3))
    },

    drawToCanvas() {
        if(!this.videoFramesInfo[this.getVideoFrame()]){
            return
        }

        const WIDTH = canvasRef.width;
        const HEIGTH = canvasRef.height;

        ctx.font = "20px Arial";
        ctx.lineWidth = 0.5;
        ctx.strokeStyle = "red";
        ctx.fillStyle = "black";

        //clear canvas to redraw everything
        ctx.clearRect(0, 0, WIDTH, HEIGTH);

        for (let element of this.videoFramesInfo[this.getVideoFrame()].elements) {
            const { x, y, h, w, elementId } = element;

            const X = x * WIDTH - (w * WIDTH) / 2;
            const Y = y * HEIGTH - (h * HEIGTH) / 2;

            ctx.strokeRect(X, Y, w * WIDTH, h * HEIGTH);
            ctx.fillText(elementId, X, Y - 2);
        }
    },

    async getVideo(projectName, videoPath) {    
        const res = await fetch("api/get-project/" + projectName);
        
        if(res.status !== 200) return "project path not found"

        const data = await res.json();
        this.videoFramesInfo = data.frames;
        this.videoMetaData = data.videoData;
    
        const res2 = await fetch("/video/" + btoa(videoPath))
        
        if(res2.status !== 200) return "video path not found"
        
        this.videoPath = "/video/" + btoa(videoPath)
        videoRef.src = this.videoPath;

        return true
    },

    setDimensions() {
        const container = /** @type {HTMLDivElement} */ (
            document.querySelector("#video-container")
        );

        canvasRef.width = container.offsetWidth;
        canvasRef.height = container.offsetHeight;

        videoRef.width = container.offsetWidth;
        videoRef.height = container.offsetHeight;
    },

    init() {
        if (this._isIinit) return;
        this._isIinit = true;

        setTimeout(()=>{
            videoRef.src = this.videoPath;
            this.setDimensions();
        }, 10)

        const gameLoop = ()=> {
            this.currentFrame = this.getVideoFrame()
            this.drawToCanvas();
            requestAnimationFrame(gameLoop);
        }
        gameLoop()          
    },
    _isIinit: false,
};

export default VideoStuff;
