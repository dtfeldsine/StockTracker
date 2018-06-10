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
    var enumerate = function(v) { var k=0; return v.map(function(e) {e._idx = k++;});};
    
    //call to get user stocks, do at beginning
    self.get_stocks = function () {
       console.log("in get_stocks");
       
       $.getJSON(get_stocks_url, function (data) {
           self.vue.stocks = data.stocks;
           self.vue.logged_in = data.logged_in;
           console.log("logged in " + self.vue.logged_in);
           enumerate(self.vue.stocks);
       })
    };
    
    
    self.init_stocks = function () {
       console.log("in init_stocks");
       $.getJSON(init_stocks_url, function (data) {
           self.vue.init_stock = data.init_stock;
       })
    };
    
    self.add_stock = function () {
        self.vue.managing_stocks = !self.vue.managing_stocks;
        console.log("adding");
        $.post(add_stock_url,
            {
                //quantity_form: self.vue.quantity_form,
                search_form: self.vue.search_form,
                name: self.vue.name,
                price: self.vue.price,
                quantity: self.vue.quantity,
            },
            //find out what this does
            function (data) {
                self.vue.stocks.unshift(data.stock);
            }
        );
    };
    
    self.add_trending = function (symbol, quantity) {
        self.vue.managing_stocks = !self.vue.managing_stocks;
        console.log("adding trending");
        $.post(add_stock_url,
            {
                search_form: symbol,
                name: self.vue.name,
                price: self.vue.price,
                quantity: self.vue.trend_quantity,
            },
            //find out what this does
            function (data) {
                self.vue.stocks.unshift(data.stock);
            }
        );
    }
    
    self.delete_stock = function(stock_id){
        console.log("deleting " + stock_id);
        $.post(del_stock_url,
            {
                id: stock_id
            },
            function () {
                var idx = null;
                for (var i = 0; i < self.vue.stocks.length; i++) {
                    if (self.vue.stocks[i].id === stock_id) {
                        idx = i + 1;
                        self.vue.stocks.splice(idx - 1, 1);
                        break;
                    }
                }
                if (idx) {
                }
            }
        );
    };
    
    // manage stocks
    self.manage_button = function () {
        console.log("javascript manage_button " + self.vue.managing_stocks);
        self.vue.managing_stocks = !self.vue.managing_stocks;
    };
    
    self.search_button = function () {
        console.log("search button pre " + self.vue.searching);
        self.vue.searching = true;
        $.post(search_url, 
            {
                //quantity_form: self.vue.quantity_form,
                search_form: self.vue.search_form,
            },
            function (data) {
                self.vue.search_list = data.search_list;
                enumerate(self.vue.search_list);
            });
        console.log("search button post " + self.vue.searching);
    };
    
    self.stock_details = function(stock_symbol){
        self.vue.in_details = true;
        $.post(stock_details_url,
            {
                sym: stock_symbol,
            },
            function (data) {
                self.vue.detail_stock = data.detail_stock;
                enumerate(self.vue.detail_stock);
            }
        )
        console.log(stock_symbol);
    };    
    
    self.back = function() {
        self.vue.in_details = false;
    };
    
    self.set_one_month = function() {
        self.vue.one_month = true;
        self.vue.three_month = false;
        self.vue.one_year = false;
        self.vue.three_year = false;
    };
    
    self.set_three_month = function() {
        self.vue.one_month = false;
        self.vue.three_month = true;
        self.vue.one_year = false;
        self.vue.three_year = false;
    };
        
    self.set_one_year = function() {
        self.vue.one_month = false;
        self.vue.three_month = false;
        self.vue.one_year = true;
        self.vue.three_year = false;
    };
        
    self.set_three_year = function() {
        self.vue.one_month = false;
        self.vue.three_month = false;
        self.vue.one_year = false;
        self.vue.three_year = true;
    };
    
    // Complete as needed.
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
           init_stock: [],
           search_list: [],
           logged_in: false,
           managing_stocks: false,
           searching: false,
           in_details: false, 
           stocks: [],
           user_email: null,
           name: "",
           price: 0,
           quantity: 0,
           trend_quantity: 0,
           search_form: "",
           detail_stock: [],
           one_month: true,
           three_month: false,
           one_year: false,
           three_year: false,
        },
        methods: {
           add_trending: self.add_trending,
           search_button: self.search_button,
           manage_button: self.manage_button,
           get_stocks: self.get_stocks,
           init_stocks: self.init_stocks,
           add_stock: self.add_stock,
           delete_stock: self.delete_stock,
           stock_details: self.stock_details,
           back: self.back,
           set_one_month: self.set_one_month,
           set_three_month: self.set_three_month,
           set_one_year: self.set_one_year,
           set_three_year: self.set_three_year,
        }

    });

    self.init_stocks();
    self.get_stocks();
    $("#vue-div").show();
    return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
