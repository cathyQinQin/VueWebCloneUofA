<template>
<div>
  <TopNavigator/>
  <MainHeader/>
  <Navigator/>
  <TopSwiper/>
  <StudyWithUs/>
  <LastestNews/>
  <suspense>
  <MoreNews/>
  </suspense>
  <ExploreCampus/>
  <suspense>
  <Footer/>
  </suspense>
</div>
</template>

<script>
import TopNavigator from './components/TopNavigator'
import MainHeader from './components/MainHeader'
import Navigator from './components/Navigator'
import TopSwiper from './components/TopSwiper'
import StudyWithUs from './components/StudyWithUs'
import LastestNews from './components/LastestNews'
import MoreNews from'./components/MoreNews'
import ExploreCampus from'./components/ExploreCampus'
import Footer from'./components/Footer'
import{onMounted} from "vue"
export default {
  name: 'App',
  components: {
    TopNavigator,
    MainHeader,
    Navigator,
    TopSwiper,
    StudyWithUs,
    LastestNews,
    MoreNews,
    ExploreCampus,
    Footer,
  },
  setup() {
    // mounted
    onMounted(() => {
      console.log('Component is mounted!')
    })
  }
}
</script>

<style>
body {
  margin: 0;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.625;
  color: #212529;
  text-align: left;
  background-color: #fff; 
}
body h1, body h2, body h3, body h4, body h5, body h6 {
    font-family: "DIN Bold",sans-serif;
    color: rgb(61, 74, 67);
    text-rendering: optimizelegibility;
}
</style>
