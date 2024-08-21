/** @param {import("alpinejs").Alpine} Alpine */
function Component(Alpine) {
    Alpine.directive("component", async (el, { expression, modifiers }, { evaluate }) => {
        const componentPath = evaluate(expression);

        const response = await fetch(`/views/${componentPath}.html`);
        const data = await response.text();

        if (modifiers.includes("outer")) {
            el.outerHTML = data;
            return;
        }

        if (modifiers.includes("inner")) {
            el.innerHTML = data;
            return;
        }

        el.innerHTML = data;
        return;
    });
}

export default Component;
