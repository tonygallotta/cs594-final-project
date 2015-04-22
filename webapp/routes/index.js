var express = require('express');
var router = express.Router();
var partials = {
  "top_nav": "top-nav",
  "head": "head",
  "sidebar": "sidebar",
  "footer": "footer"
};
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', {partials: partials, intro: true});
});

router.get('/tasks', function(req, res, next) {
  res.render('tasks', {partials: partials, tasks: true});
});

router.get('/data', function(req, res, next) {
  res.render('data', {partials: partials, data: true});
});

router.get('/software', function(req, res, next) {
  res.render('software', {partials: partials, software: true});
});

router.get('/hardware', function(req, res, next) {
  res.render('hardware', {partials: partials, hardware: true});
});

router.get('/results', function(req, res, next) {
  res.render('results', {partials: partials, results: true});
});

module.exports = router;
