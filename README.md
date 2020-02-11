To run locally:
```
bundle install
bundler exec jekyll serve --future
```

Can use --incremental to try to only build diffs, but unreliable:
```
bundler exec jekyll serve --future --incremental
```

To build JS:
```
npm run-script uglify
```
