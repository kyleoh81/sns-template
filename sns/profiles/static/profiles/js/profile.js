Vue.options.delimiters = ['[[', ']]']

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

params = new URLSearchParams();
meta = {
    headers: {"Content-Type": 'application/x-www-form-urlencoded'}
}

const follow = new Vue({
    el: "#v-follow",
    data: function(){
        return {
            toggle: true,
        }
    },
    methods: {
        change: function(event){
            this.toggle = ! this.toggle
        },
        follow: function(pk){
            axios.put("/api/follows/" + pk + "/", params, meta)
            .then(function(res){
                this.change()
            }.bind(this))
        },
        unfollow: function(pk){
            axios.delete("/api/follows/" + pk + "/", params, meta)
            .then(function(res){
                this.change()
            }.bind(this))
        },
    },
})

