
# Run locally

Requires:
+ bundler
+ ruby
+ ruby-devel

```
gem install nokogiri -- --use-system-libraries
bundle install
bundle add webrick
bundle exec jekyll serve --future
```

Can use --incremental to try to only build diffs, but unreliable:
```
bundler exec jekyll serve --future --incremental
```
