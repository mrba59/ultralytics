import Alpine from "./alpine-plugins/register-alpine-plugins.js";
import VideoStuff from "./video-stuff.js";

Alpine.store("video", VideoStuff);

Alpine.start();