Vue.options.delimiters = ['[[', ']]']


Vue.component("status-card", {
    template: "#status-card",
    props: ["status"],
    data: function(){
        return {
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

