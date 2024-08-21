import { Alpine } from "../../libs/alpine.esm.js";
import { persist } from "../../libs/alpine-persist.esm.js";
import Component from "./components-plugin.js";

Alpine.plugin(persist);
Alpine.plugin(Component);

//@ts-ignore binds apine to the global scope
window.Alpine = Alpine;

export default Alpine;
