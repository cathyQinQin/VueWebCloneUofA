<template>
    <div class="banner-container">
        <div class="explore-uofa-campuses">
            <div class="lougheed">
                <h2><a data-feature="Explore Our Campuses" href="campus-life/our-campuses/index.html">Explore our campuses</a></h2>
                <p>The University of Alberta is a busy place — 38,000 students across 18 faculties at five separate campus locations. Learn about each of the unique campuses that make up the fifth largest university in Canada.</p>
                <a class="yo btn" data-feature="Explore Our Campuses" href="campus-life/our-campuses/index.html">Our Campuses</a>
            </div>
        </div>
        <div class="social">
            <div class="keep-in-touch">
                <h3>Give to the U of A</h3>
                <div class="no-gutters">
                    <i class="fas fa-heart"></i>
                    <div>
                        <p>The University of Alberta is building one of the world's great universities for the public good. Your gift accelerates our work.&nbsp;</p>
                        <p><a href="https://www.ualberta.ca/giving/index.html">Give to the University of Alberta<span>&nbsp;</span>»</a></p>
                    </div>
                </div>
            </div>
            <div class="keep-in-touch">
                <h3>Careers</h3>
                <div class="no-gutters">
                    <i class="fas fa-toolbox"></i>
                    <div>
                        <p>We employ faculty and staff across five campuses, making us one of the largest employers in the Province of Alberta.</p>
                        <p><a href="https://www.careers.ualberta.ca/" rel="noopener" target="_blank">Search Career Opportunities <span>&nbsp;</span>» </a></p>
                    </div>
                </div>
            </div>
        </div>
        <div class="new-explore-bar">
            <div class="icon">
                <i class="fas fa-dragon"></i>
                <a href="https://www.ualberta.ca/aboriginal-indigenous">Aboriginal / Indigenous </a>
            </div>
            <div class="icon">
                <i class="far fa-calendar-alt"></i>
                <a href="https://calendar.ualberta.ca/">University Calendar </a>
            </div>
            <div class="icon">
                <i class="fas fa-home"></i>
                <a href="https://www.residence.ualberta.ca">Residence / Housing </a>
            </div>
            <div class="icon">
                <i class="fas fa-store"></i>
                <a href="https://bookstore.ualberta.ca/"> Bookstore </a>
            </div>
            <div class="icon">
                <i class="fas fa-trophy"></i>
                <a href="https://www.ualberta.ca/athletics"> Athletics </a>
            </div>
            <div class="icon">
                <i class="fas fa-swimmer"></i>
                <a href="https://www.ualberta.ca/kinesiology-sport-recreation/campus-community-recreation/index.html">Recreation </a>
            </div>
        </div>
    </div>
</template>
<style scoped>
.explore-uofa-campuses{
    color: #fff;
    background: #93999f url(https://www.ualberta.ca/media-library/ualberta/homepage/north-campus-quad.jpg);
    background-size: cover;
    background-repeat: no-repeat;
    background-position: 0% 55%;
    height: 577px;
}
.lougheed{
    height: 100%;
    width: 50%;
    background: linear-gradient(to left, rgba(0,0,0,0) 0%,rgba(0,0,0,0.5) 75%);
    padding: 12.5% 10% 15% 10%;
}
.lougheed a{
    color: #fff;
    text-decoration: none;
    text-shadow: 3px 3px 6px #000000;
}
.lougheed a:hover {
    text-decoration: underline;
}
.lougheed p{
    margin-bottom: 0;
    font-size: 1.5vw;
    line-height: 1.25em;
}
.explore-uofa-campuses a.yo {
    padding: 0.5em 2.25em;
    border-radius: 6px;
    transition: background-color 200ms ease,color 200ms ease;
    font-family: "DIN Bold", sans-serif;
    text-shadow: none;
    background-color: #ffffff;
    color: #404545;
    margin-top: 1.25em;
    font-weight: 800;
}
.explore-uofa-campuses a.yo:hover {
    background-color: #dddddd;
    color: #404545;
    text-decoration: none;
}
.social{
    display: flex;
    background-color: #ECBE13;
    padding: 50px 11% 50px 11%;
    color: #3d4a43;
}
.social h3{
    font-size: 1.375rem;
    margin-bottom: 1rem;
    font-weight: 500;
    line-height: 1.25;
}
.social i{
    font-size: 6em;
    padding-right: 30px;
}
.social p a {
    text-decoration: none;
    color: #3d4a43;
}
.social p a:hover {
    text-decoration: underline;
}
.no-gutters{
    display: flex;
}
.new-explore-bar{
    display: flex;
    background-color: #2E6A3B;
    padding: 50px 11% 50px 11%;
}
.new-explore-bar a{
    text-decoration: none;
    color: #fff;
    font-family: 'DIN MEDIUM', sans-serif;
}
.new-explore-bar a:hover{
    text-decoration: underline;
}
.new-explore-bar i{
    font-size: 2.5rem;
}
.new-explore-bar .icon:first-child{
    align-items: flex-start;
}
.new-explore-bar .icon{
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: #fff;
}
</style>