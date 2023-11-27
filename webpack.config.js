const path = require('path');

module.exports = {
    entry: './resources/js/app.js',    
    output: {
        path: path.resolve(__dirname, './public/assets'),
        filename: 'bundle.js'    
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                    'style-loader',
                    'css-loader',
                ],
            },
        ],
    },
};