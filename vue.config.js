modules.exports = {
  lintOnSave: false,
  publicPath: '/',
  devServer: {
    proxy: {
      '/seeyon': {
        target: proxySite,
        changeOrigin: true,
        pathRewrite: {
          '^/seeyon': '',
        },
      },
    },
  },
};