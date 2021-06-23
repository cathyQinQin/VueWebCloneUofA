<template>
    <div>
        <nav class="navbar-wrapper">
            <div class="my-navbar">
                <a class="item " href="https://apps.ualberta.ca/directory">Find a Person</a>
                <a class="item " href="https://www.onecard.ualberta.ca/">ONEcard</a>
                <a class="item " href="https://www.beartracks.ualberta.ca/">Bear Tracks</a>
                <a class="item " href="https://www.ualberta.ca/maps">Maps</a>
                <a class="item " href="https://apps.ualberta.ca/">Email &amp; Apps</a>
                <a class="item " href="https://eclass.srv.ualberta.ca/portal/">eClass</a>
                <a class="item " href="https://www.library.ualberta.ca/">Library</a>
            </div>
            <button class="btn btn-toggle" @click="open = !open">
                <i class="fas" :class="open ? 'fa-times' : 'fa-search'" />
            </button>
        </nav>
        <div v-if="open">
            <div class="drop-item-wrapper">
                <div class="search-wrapper">
                    <h2>Search</h2>
                    <div class="form-check form-check-inline">
                        <input v-model="picked" class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1">
                        <label class="form-check-label" for="inlineRadio1">All</label>
                    </div>
                    <div class="form-check form-check-inline">
                        <input v-model="picked" class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="option2">
                        <label class="form-check-label" for="inlineRadio2">People</label>
                    </div>
                </div>
                <div class="input-search-bar-wrapper">
                    <input 
                        type="search" 
                        class="input-search-bar" 
                        v-bind:placeholder="placeholder" 
                        v-model="searchText"
                    />
                    <a class="my-btn" role="button" @click="search">Search</a>
                </div>
                <div class="popular-queries">
                    <h4>Popular Queries</h4>
                    <a class="coveo-keywords" href="https://www.ualberta.ca/search#q=engineering">engineering</a><a class="coveo-keywords" href="https://www.ualberta.ca/search#q=science">science</a><a class="coveo-keywords" href="https://www.ualberta.ca/search#q=professor">professor</a><a class="coveo-keywords" href="https://www.ualberta.ca/search#q=graduate">graduate</a><a class="coveo-keywords" href="https://www.ualberta.ca/search#q=management">management</a>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import { ref, computed} from "vue"

export default {
    setup() {
        const open = ref(false)
        
        const searchText = ref("")

        const picked = ref("option1")

        const placeholder = computed(()=> picked.value == "option1" 
            ? "Search Ualberta websites" 
            : "Search by name, title, phone number, keyword" 
        )

        function search(){
            let query = picked.value == "option1" ? "Main" : "People"
            window.location.assign(`https://www.ualberta.ca/search/index.html#q=${searchText.value}&t=${query}&sort=relevancy`)
        }

        return {
            open,
            searchText,
            search,
            picked,
            placeholder
        }
    },
}
</script>


<style scoped>
    .btn-toggle {
        margin-left: 16px;
        background-color: #ffdb05;
        border-radius: 50%;
        width : 40px;
        height: 40px;
        font-size: 20px;
        font-weight: 400;
        color : black;
        padding: 0;
    }

   .btn-toggle:active, .btn-toggle:hover {
        background-color: #d8b906;
        border-color: #d8b906;
    }
    a {
        color: #707070;
        text-decoration: none;
    }
    a.item {
        font-size: 0.875rem;
        padding: .5rem .4rem;
        display : inline-block;
        font-weight: 400;
    }

    a.item:hover {
        text-decoration: underline;
    } 
    .navbar-wrapper{
        display: flex;
        justify-content: flex-end;
        box-sizing: border-box;
        align-items: center;
        height: 72.67px;
        padding: .5rem 9%;
    }
    .my-navbar{
        display: flex;
        padding: .5rem .4rem;
        box-sizing: border-box;
        align-items: center;        
        font-family: sans-serif;
    }
    .drop-item-wrapper{
        box-sizing: border-box;
        height: 239px;
        padding: 2rem 9% 42px;
        display: flex;
        flex-direction: column;
        flex: 1,1,0;
        border: 1px solid #DDD;
    }
    .search-wrapper{
        display: flex;
        flex: 1;
    }
    input[type="radio"]:checked {
            border-color: #007C41;
            background-color: #007C41;
    }
    input[type="radio"]:active {
        border-color: #30ff9c;
        background-color: #30ff9c;
    }
    input[type="radio"]:focus {
        box-shadow: none;
    }
    h2{
        font-size: 1.5rem;
        margin-bottom: 1rem;
        font-weight: 500;
        padding-right: 2rem;
    }
    .input-search-bar-wrapper{
        display: flex;
        flex: 1;
    }
    .input-search-bar{
        flex: 1;
        border: 1px solid #bcc3ca;
        outline: none;
        padding: 12px 0;
        text-indent: 12px;
        background: #eef3f0;
    }
    .my-btn{
        display: flex;
        justify-content: center;
        align-items: center;
        color: #fff;
        background-color: #007c41;
        width: 100px;
        font-size: 18px;
        font-weight: 500;
        border: 1px solid #bcc3ca;
        text-decoration: none;
    }
    .popular-queries{
        display: flex;
        flex: 1;
        align-items: flex-end;
    }
    .coveo-keywords{
        border-radius: 10px;
        background: #eef3f0;
        color: #003019;
        font-size: 90%;
        padding: 1px 8px;
        margin-right: 2px;
        margin-bottom: 5px;
    }
    h4{
        padding-right: 10px;
    }
</style>