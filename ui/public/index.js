import Alpine from "./scripts/alpine-plugins/register-alpine-plugins.js";
import VideoStuff from "./scripts/video-stuff.js";

Alpine.store("video", VideoStuff);

Alpine.start();
