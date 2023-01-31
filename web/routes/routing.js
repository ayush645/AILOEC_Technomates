// File to define routes

const express = require('express');
const router = express.Router();
const controller = require('../containers/form');
router.get('/',controller.home)
router.get('/form', controller.form);
router.post('/form', controller.formprocess);
router.get('/approved',controller.approved)
router.get('/napproved',controller.napproved)

module.exports = router