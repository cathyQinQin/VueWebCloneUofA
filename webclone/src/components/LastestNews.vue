<template>
<div>
    <h2 class="latest-news-header">Honouring National Indigenous History Month</h2>
    <div class="latest-news-container">
        <div class="story-card">
            <div class="story-container">
                <div class="image-wrapper">
                    <img 
                        class="story-image" 
                        src="https://www.ualberta.ca/news/media-library/week-in-review/nation-indigenous-history-month.png"
                    />
                    <div class="image-title">UNIVERSITY NEWS</div>
                    <div class="image-bottom"></div>
                </div>
                <h4 class="story-title">
                <a class="stretched-link" href="https://www.ualberta.ca/equity-diversity-inclusivity/initiatives/national-indigenous-history-month.html">
                    National Indigenous History Month 
                </a>
                </h4>
                <div class="story-teaser">
                    Learn about the compassionate, curious, and creative Indigenous community members who have led with purpose to inspire a more just and interconnected society for both today and tomorrow. 
                </div>
                <div class="story-date">
                    June 01, 2021
                </div>
            </div>
            <div class="story-container">
                <div class="image-wrapper">
                    <img alt="Folio" class="folio-logo" src="https://www.ualberta.ca/news/media-library/logos/reverse/folio-logo-reverse.svg">
                    <img class="story-image" src="https://www.ualberta.ca/folio/media-library/2021/06/210603-congress-indigenous-scholarship-florence-glanfield-teaser-16x9-3000px1.jpg">
                    <div class="image-bottom"></div>
                </div>
                <h4 class="story-title">
                <a class="stretched-link" href="https://www.ualberta.ca/folio/2021/06/engaging-in-ethical-community-based-research-congress-2021-session-helps-researchers-practise-indigenous-engaged-scholarship.html">
                    From the President's Desk: Honouring National Indigenous History Month 
                </a>
                </h4>
                <div class="story-teaser">
                    SKIPP offers a space to discuss ethical and respectful research as part of “Career Corner” series at virtual conference.
                </div>
                <div class="story-date">
                    June 03, 2021
                </div>
                
            </div>
        </div>
    </div>
</div>
</template>
<style scoped>
    .latest-news-header{
        margin: 2rem 0;
        font-size: 2.143rem;
        text-align: center;
        font-weight: 500;
        line-height: 1.25;
    }
    h2.latest-news-header{
        font-weight: 600;
    }
    .latest-news-container{
        display: flex;
        padding: 0 8%;
    }
    .image-wrapper{
        height: 400px;
        overflow: hidden;
        position: relative;
    }
    .image-wrapper .image-title{
        position : absolute;
        bottom : 1%;
        left : 1%;
        height: 25px;
        color: white;
        font-family: 'DIN Bold', sans-serif;
        z-index: 100;
    }
    .image-wrapper .image-bottom{
        position: absolute;
        bottom: 0;
        background: linear-gradient(transparent, black);
        height: 50px;
        width: 100%;
        z-index: 1;
    }
    img.story-image{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: 1.2s transform;
    }
    .story-container:hover .story-image{
        transform: scale(1.2);
    }
    .folio-logo{
        position: absolute;
        height: 25px;
        z-index: 100;
        bottom: 1%;
        left: 1%;
    }    
    .story-card{
        display: flex;
        border-bottom: 1px solid #CCCCCC;
        padding-bottom: 2%;
    }
    .story-container {
        flex: 0 0 50%;
        padding:0 18px;
        border-right: 1px solid #CCCCCC;
    }
    .story-container:first-child{
        padding-left: 0;
    }
    .story-container:last-child{
        border-right: 0;
        padding-right: 0;
    }
    .story-container .story-title{
        margin: 1rem 0;
        font-weight: 600;
        font-size: 1.25rem;
        font-family: 'Merriweather', serif;
    }
    .story-container .stretched-link{
        text-decoration: none;
        color: #11151c;
        transition: color 1.2s;
    }
    .story-container .stretched-link:hover{
        color:#007c41;
    }
    .story-container .story-date{
        margin-top: 1rem;
    }
</style>