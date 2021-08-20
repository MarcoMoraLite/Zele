odoo.define(" ", fuction(require) {
    "use strict";

    var ajax = require("web.ajax");

    $(document).ready(fuction() {
        $(" ").bind("click", fuction(ev) {
            var ine_base = $(" ");
            ajax.jsonRpc(" ", "call", {
                imag: ine_base,
            });
        });
    });
});