const webpack = require('webpack');

module.exports = {
  resolve: {
    fallback: {
      path: require.resolve('path-browserify'),
      util: require.resolve('util/'),
      assert: require.resolve('assert/'),
      fs: false,
      perf_hooks: false,
      worker_threads: false,
      url: false,
    },
  },
  plugins: [
    new webpack.ProvidePlugin({
      process: 'process/browser',
    }),
  ],
};
