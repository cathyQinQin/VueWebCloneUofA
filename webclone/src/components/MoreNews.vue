<template>
    <div>
        <h2 class="latest-news-header">
            <a href="https://www.ualberta.ca/news/index.html">Latest News &amp; Stories</a>
        </h2>
        <div id="stories">
            <p>Featured Topics: <a class="filter-link" data-link="https://www.ualberta.ca/api/coveo/search/ualberta-news-feed?count=50&amp;" href="#stories">All</a> | <a href="https://www.ualberta.ca/news/covid-19/index.html">COVID-19</a> | <a href="https://www.ualberta.ca/news/innovation/index.html">Innovation</a> | <a class="filter-link" data-link="https://www.ualberta.ca/api/coveo/search/ualberta-news-feed?news_theme=('Health')&amp;" href="#stories">Health</a></p>
        </div>
        <div class="story-wrapper" :style="{height: extendableHeight}">
            <div class="story-column" v-for="(data, i) in datas" :key="i">
                <div class="story" v-for="(story, i) in data" :key="i">
                    <div class="story-image-wrapper">
                        <img :src="story['cover_image']" class="cover-image"/>
                        <img class="logo" :src="story['cover_logo']">
                        <div class="image-bottom"></div>
                    </div>
                    <div class="story-category">
                        {{story['category']}}
                    </div>
                    <div class="story-title">
                        <a :href="story['title_link']">
                            {{story['title_text']}}
                        </a>
                    </div>
                    <div class="story-teaser">
                        {{story['story_teaser']}}
                    </div>
                    <div class="story-date">
                        {{story['story_date']}}
                    </div>
                </div>
            </div>
        </div>
        <div class="load-more-button">
            <button class="btn" @click="extendHeight">View More News &amp; Stories</button>
        </div>
        <div class="uofa-social-connect">
            <h2>Keep In Touch</h2>
            <a href="https://www.facebook.com/ualberta"> 
                <i class="fab fa-facebook-f"></i>&nbsp;Facebook</a>&emsp;|&emsp;
            <a href="https://twitter.com/UAlberta">
                <i class="fab fa-twitter"></i>&nbsp;Twitter</a>&emsp;|&emsp;
            <a href="https://www.linkedin.com/school/6455/">
                <i class="fab fa-linkedin-in"></i>&nbsp;Linkedin</a>&emsp;| &emsp;
            <a href="https://www.instagram.com/ualberta/">
                <i class="fab fa-instagram"></i>&nbsp;Instagram</a>&emsp;|&emsp;
            <a href="https://www.youtube.com/user/UniversityofAlberta">
                <i class="fab fa-youtube"></i>&nbsp;Youtube</a>
        </div>             
        <div class="upcoming-events-header">
            <h2>Upcoming Events</h2>
        </div>
        <div class="events-container">
            <div class="event">
                <div class="event-photo"><a href="https://www.ualberta.ca/human-resources-health-safety-environment/employment-information/information-for-new-employees/faculty-staff-orientation-event.html" rel="noopener" target="_blank" title="Faculty and Staff Orientation Networking Event"> <img alt="" height="350" src="https://www.ualberta.ca/media-library/ualberta/events/uofa-north-campus-signage-closeup.jpg"> </a>
                </div>
                <div class="event-date-container"><span class="event-date">Jun 23</span> <span class="event-time">9 AM</span>
                </div>
                <div class="event-title"><a href="https://www.ualberta.ca/human-resources-health-safety-environment/employment-information/information-for-new-employees/faculty-staff-orientation-event.html" rel="noopener" target="_blank">Faculty and Staff Orientation Networking Event</a>
                </div>
            </div>
            <div class="event">
                <div class="event-photo"><a href="https://www.ualberta.ca/events/augustana/110/imaginenative-110.html" rel="noopener" target="_blank" title="2021 imagineNATIVE Presents: Short Films Focus"> <img alt="" height="350" src="https://www.ualberta.ca/media-library/ualberta/events/imaginenative.jpg"> </a>
                </div>
                <div class="event-date-container"><span class="event-date">Jun 23</span> <span class="event-time">5 PM</span>
                </div>
                <div class="event-title"><a href="https://www.ualberta.ca/events/augustana/110/imaginenative-110.html" rel="noopener" target="_blank">2021 imagineNATIVE Presents: Short Films Focus</a>
                </div>
            </div>
            <div class="event">
                <div class="event-photo"><a href="https://docs.google.com/forms/d/1ixUXZ6y0ud7yvHBYRVYymGX-m6G0j6PbOjTIdtzkYS8/viewform" rel="noopener" target="_blank" title="PowwowFIT with Notorious Cree"> <img alt="" height="350" src="https://www.ualberta.ca/media-library/ualberta/events/notorious-cree-550x350.jpeg"> </a>
                </div>
                <div class="event-date-container"><span class="event-date">Jun 24</span> <span class="event-time">1 PM</span>
                </div>
                <div class="event-title"><a href="https://docs.google.com/forms/d/1ixUXZ6y0ud7yvHBYRVYymGX-m6G0j6PbOjTIdtzkYS8/viewform" rel="noopener" target="_blank">PowwowFIT with Notorious Cree</a>
                </div>
            </div>
        </div>
        <div class="more-events">
            <a href="https://www.ualberta.ca/events/index.html">View More Events »</a>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import { computed, ref } from '@vue/runtime-core';
export default {
    async setup() {
        let datas = [];
        await axios.get('./data/data.json').then((res) => {
        datas = res.data;
        }) 
        let height = ref(500);
        const extendableHeight = computed(() => height.value + 'px');
        function extendHeight(){
            const addHeight = 500;
            height.value += addHeight;
        }
        return{
            datas,
            extendableHeight,
            extendHeight
        }
    },
}
</script>
<style scoped>
    .latest-news-header {
        font-size: 2.143em;
        text-align: center;
        margin: 2rem 0 1rem 0;
    }
    .latest-news-header a {
        transition: .2s color; 
        color: #3d4a43;;
        text-decoration: none;
    }
    .latest-news-header a:hover {
        color: #007c41;
        text-decoration: none;
    }
    #stories{
        text-align: center;
    }
    #stories a{
        color: #007c41;
        text-decoration: none;
    }
    #stories a:hover {
        color: #003019;
        text-decoration: underline;
    }
    .story-wrapper{
        display: flex;
        padding: 0 8%;
        overflow: hidden;
    }
    .story-column{
        flex: 1 1 100%;
        border-right: 1px solid #CCCCCC;
        padding: 0 18px;
    }
    .story-column:first-child{
        padding-left: 0;
    }
    .story-column:last-child{
        border-right: 0;
        padding-right: 0;
    }
    .story{
        padding-bottom: 24px;
        margin-bottom: 24px;
        border-bottom: 1px solid #CCCCCC;
    }
    .story-image-wrapper{
        overflow: hidden;
        position: relative;
    }
    .story img.cover-image{
        width: 100%;
        height: 100%;
        transition: 1.2s transform;
    }
    .story:hover .cover-image {
        transform: scale(1.2);
    }
    .image-bottom{
        position: absolute;
        bottom: 0;
        background: linear-gradient(transparent, black);
        height: 50px;
        width: 100%;
        z-index: 1;
    }
    .story-image-wrapper .logo{
        position : absolute;
        bottom : 1%;
        left: 1%;
        height: 25px;
        color: white;
        font-family: 'DIN Bold', sans-serif;
        z-index: 100;
    }
    .story-category{
        margin: 10px 0;
        color: #707070;
        font-size: 12px;
        text-transform: uppercase;
    }
    .story-title{
        font-weight: 800;
        font-size: 1.25rem;
        font-family: 'Merriweather', serif;
    }
    .story-title a{
        color: #11151c;
        transition: .2s color;
        text-decoration: none;
    }
    .story-title a:hover {
        color: #007c41;
    } 
    .story-teaser{
        font-size: 1rem;
        margin-bottom: 1rem;
    }
    .load-more-button{
        display: flex;
        justify-content: center;
        border-top: 1px solid #CCCCCC;
    }
    .load-more-button button{
        text-align: center;
        margin-top: 36px;
        margin-bottom: 36px;
        font-weight: 800;
        font-size: .8rem;
        padding: 0.5rem 0;
        width: 216px;
        height: 45px;
        color: #fff;
        background-color: #007c41;
        border-color: #007c41;
        font-family: "DIN Bold",sans-serif;  
    }
    .uofa-social-connect{
        margin: 0 8%;
        background: #f5f8f6;
        text-align: center;
        padding: 50px;
        margin-bottom: 50px;
    }
    .uofa-social-connect h2{
        margin-bottom: 1rem;
        font-weight: 500;
        line-height: 1.25;
        font-size: 1.5rem;
    }
    .uofa-social-connect a{
        color: #007C41;
        text-decoration: none;
    }
    .uofa-social-connect a:hover {
        color: #003019;
        text-decoration: underline;
    }
    .upcoming-events-header h2{    
        font-size: 2.143em;
        font-family: 'DIN Bold', sans-serif;
        text-align: center;
        margin: 2rem 0;
        font-weight: 600;
    }
    .events-container{
        display: flex;
        padding: 0 8%;
    } 
    .event{
        flex: 1;
        padding: 0 3%;
        position: relative;
    }   
    .event-photo{
        margin-bottom: .5rem;
    }
    .event-photo img{
        width: 100%;
        height: 100%;
    }
    .event-title a{
        text-decoration: none;
        color: #3d4a43;
        margin-top: 0.5em;
        font-family: "DIN Bold",sans-serif;
        font-weight: 600;
    }
    .event-date-container{
        display: flex;
        flex-direction: column;
        position: absolute;
        top: 15%;
        padding: 10px;
        background-color: #fff;
        text-align: center;
        opacity: 0.85;
    }
    .more-events{
        text-align: center;
        margin: 2rem 0;
    }
    .more-events a{
        color: #007c41;
        text-decoration: none;
    }
    .more-events a:hover{
        color: #003019;
        text-decoration: underline;
    }
</style>