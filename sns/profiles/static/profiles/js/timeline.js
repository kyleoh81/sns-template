Vue.options.delimiters = ['[[', ']]']

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

params = new URLSearchParams();
meta = {
    headers: {"Content-Type": 'application/x-www-form-urlencoded'}
}

Vue.component("status-card", {
    template: "#status-card",
    props: ["status"],
    data: function(){
        return {
        }
    },
    methods: {
        like: function(event){
            axios.put("/api/likes/" + this.status.pk + "/", params, meta)
            .then(function(res){
                this.status.is_liked = res.data.is_liked
            }.bind(this))
        },
        stoplike: function(event){
            axios.delete("/api/likes/" + this.status.pk + "/", params, meta)
            .then(function(res){
                this.status.is_liked = res.data.is_liked
            }.bind(this))
        }
    },
})

Vue.component("timeline", {
    template: "#timeline",
    props: ["url"],
    data: function(){
        return {
            statuses: [],
        }
    },
    created: function(){
        axios.get(this.url)
        .then(function(res){
            this.statuses = res.data
        }.bind(this))
    }
})
new Vue({el: "#v-timeline"})
