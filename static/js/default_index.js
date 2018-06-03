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
    
    //call to get user stocks, do at beginning
    self.get_stocks = function () {
       console.log("in get_stocks");
       $.getJSON(get_stocks_url, function (data) {
           self.vue.logged_in = data.logged_in;
           self.vue.stocks = data.stocks;
       })
    };
    
    // manage stocks
    self.manage_button = function () {
        console.log("javascript manage_button " + self.vue.managing_stocks);
        self.vue.managing_stocks = !self.vue.managing_stocks;
    };

    // Complete as needed.
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
           logged_in: false,
           managing_stocks: false,
           stocks: [],
           user_email: null,
        },
        methods: {
           manage_button: self.manage_button,
           get_stocks: self.get_stocks,
        }

    });

    
    self.get_stocks();
    $("#vue-div").show();
    return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
