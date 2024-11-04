<template :class="['app-container', isDark ? 'bg-dark text-white' : 'bg-light']">
  <div 
    id="app-wrapper"
    :class="['app-container', isDark ? 'bg-dark text-white' : 'bg-light']"
  >
    <h1>Hello World</h1>
  </div>
</template>



<script>
  import { mapState, mapActions } from 'vuex';

  export default {
    name: 'App',
    components: { },
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