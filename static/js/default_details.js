// This is the js for the default/index.html view.

var app = function() {

    var self = {};

    Vue.config.silent = false; // show all warnings

    // Extends an array
    self.extend = function(a, b) {
        for (var i = 0; i < b.length; i++) {
            a.push(b[i]);
        }
    };
    
    // Enumerates an array.
    var enumerate = function(v) { var k=0; return v.map(function(e) {e._idx = k++;});};    // Complete as needed.
    
    self.get_stock = function () {
       console.log("in get_stocks");
       
       $.getJSON(get_stock_url, function (data) {
           self.vue.stocks = data.stocks;
           enumerate(self.vue.stocks);
       })
    };
    
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            stocks: [],
        },
        methods: {
            get_stock: self.get_stock,
        }
    
    });
    
    self.get_stock();
    $("#vue-div").show();
    return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});