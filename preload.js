fs = require('fs')

const parent = {
    FM: {
        view: (obj) => {
            fs.writeFileSync('414.html', obj.html)
        }
    }
}

module.exports = parent
