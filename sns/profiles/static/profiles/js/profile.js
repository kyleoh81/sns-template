Vue.options.delimiters = ['[[', ']]']

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
const params = new URLSearchParams();
const meta = {
    headers: {"Content-Type": 'application/x-www-form-urlencoded'}
}

const sc = Vue.component("status-card", {
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

const timeline = new Vue({
    el: "#v-timeline",
    data: function(){
        return {
            statuses: [],
        }
    },
    created: function(){
        axios.get(url)
        .then(function(res){
            this.statuses = res.data
        }.bind(this))
    }
})

