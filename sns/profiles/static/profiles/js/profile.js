Vue.options.delimiters = ['[[', ']]']

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

params = new URLSearchParams();
meta = {
    headers: {"Content-Type": 'application/x-www-form-urlencoded'}
}

Vue.component("user-profile", {
    template: "#user-profile",
    props: ["user"],
    data: function(){
        return {
        }
    },
    methods: {
        change: function(event){
            this.user.is_followed = ! this.user.is_followed
        },
        follow: function(pk){
            axios.put("/api/follows/" + this.user.pk + "/", params, meta)
            .then(function(res){
                this.change()
            }.bind(this))
        },
        unfollow: function(pk){
            axios.delete("/api/follows/" + this.user.pk + "/", params, meta)
            .then(function(res){
                this.change()
            }.bind(this))
        },
    },
})

Vue.component("users", {
    template: "#users",
    props: ["url"],
    data: function(){
        return {
            users: []
        }
    },
    created: function(){
        axios.get(this.url)
        .then(function(res){
            this.users = res.data
        }.bind(this))
    }
})
new Vue({el: "#v-users"})

Vue.component("profile-full", {
    template: "#profile-full",
    props: ["url"],
    data: function(){
        return {
            user: {},
        }
    },
    created: function(){
        axios.get(this.url)
        .then(function(res){
            this.user = res.data
        }.bind(this))
    }
})
new Vue({el: "#v-profile-full"})
