import { createStore } from 'vuex';



export default createStore({
    state: {
        isDark: localStorage.getItem('theme') === 'dark' || localStorage.getItem('theme') === null
    },

    mutations: {
        toggleTheme(state) {
            state.isDark = !state.isDark;
            localStorage.setItem('theme', state.isDark ? 'dark' : 'light');
        }
    },

    actions: {
        toggleTheme({ commit }) {
            commit('toggleTheme');
        }
    }
});