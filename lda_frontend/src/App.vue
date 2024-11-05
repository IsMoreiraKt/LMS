<template :class="['app-container', isDark ? 'bg-dark text-white' : 'bg-light']">
  <div 
    id="app-wrapper"
    :class="['app-container', isDark ? 'bg-dark text-white' : 'bg-light']"
  >
    <HeaderComponent/>
  </div>
</template>



<script>
  import { mapState, mapActions } from 'vuex';
  import HeaderComponent from './components/HeaderComponent.vue'

  export default {
    name: 'App',
    components: {
      HeaderComponent,
    },
    computed: {
      ...mapState(['isDark'])
    },
    methods: {
      ...mapActions(['toggleTheme'])
    }
  }
</script>



<style>
  * {
    margin: 0;
    padding: 0;

    box-sizing: border-box;
  }

  .app-container {
    width: 100vw;
    height: 100vh;
  }
</style>