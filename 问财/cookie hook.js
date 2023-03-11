 var v = "";
Object.defineProperty(document, "cookie", {
    set: function(val){ // 在对 document.cookie = xxxx
        debugger; // 断点
        v = val;
        return v;
    },
    get(){ // 在使用document.cookie
        return v;
    }
})