vm = new Vue({
    el: '#view_root',
	data: {
        columns: {name:"商品名", description:"説明", price:"価格", stock:"在庫"},
        items: [{name: "Now loading", description: "Now loading", price: "0 YEN", stock: "0"}],
	},
    mounted(){
        axios.get('/items.php?minstock=0')
            .then(function (response) {
                console.log(vm.$data);
                vm.$data.items = response.data;
            })
            .catch(function (error) {
                console.log(error);
            });
    }
})

