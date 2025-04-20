import { createStore } from 'vuex';

export default createStore({
  state: {
    isHidden: true, // 用于追踪是否单击了"隐藏"
    showContent: true,
  },
  mutations: {
    setHide(state, payload) {
      state.isHidden = payload;
    },
    setShowContent(state, payload) {
      state.showContent = payload;
    },
  },
});