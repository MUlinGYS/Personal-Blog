import { createStore } from 'vuex';

export interface State { // 添加 export 关键字
  showContent: boolean;
  isHidden: boolean;
}

export default createStore<State>({
  state: {
    isHidden: true, // 用于追踪是否单击了“隐藏"
    showContent: true,
  },
  mutations: {
    setHide(state, payload: boolean) {
      state.isHidden = payload;
    },
    setShowContent(state, payload: boolean) {
      state.showContent = payload;
    },
  },
});