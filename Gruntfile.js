
module.exports = function(grunt) {

  grunt.initConfig({

    watch: {
      styles: {
        files: '_public/css/*.css',
        tasks: ['postcss']
      },
      grunt: {
        files: 'Gruntfile.js'
      },
      options: {
        spawn: false
      }
    },
    postcss: {
      options: {
        processors: [
          require('precss')(),
          require('autoprefixer-core')(),
          require('cssnano')()
        ]
      },
      dist: {
        src: '_public/css/*.css',
        dest: 'app/static/css/main.min.css'
      }
    },
    imagemin: {
      static: {
        optimizationLevel: 3
      },
      dynamic: {
        expand: true,
        cwd: '_public/img/',
        src: ['*.{png,jpg,gif}'],
        dest: 'app/static/img/'
      }
    },

    browserSync: {
      dev: {
        bsFiles: {
          src : [
            'app/static/css/*.css',
            'app/templates/*.html'
          ]
        },
        options: {
          watchTask: true,
          proxy: 'localhost:8000'
        }
      } 
    }

  });

  grunt.loadNpmTasks('grunt-contrib-imagemin');
  grunt.loadNpmTasks('grunt-postcss');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-browser-sync');

  grunt.registerTask('default', ['browserSync', 'watch']); 

};

