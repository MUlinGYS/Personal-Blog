modules.exports = {
  lintOnSave: false,
  publicPath: './',
  configureWebpack: {
    resolve: {
      alias: {
        '@': 'src'
      }
    }
  },
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