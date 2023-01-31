// Express is a minimal and flexible Node.js web application framework that provides a robust
// set of features to develop web and mobile applications. 
// It facilitates the rapid development of Node based Web applications

const { json } = require('body-parser');
const express = require('express');
const qs = require('qs');
const axios = require('axios');

// module to handle get request on localhost:3000 and load the registration form
exports.home = (req, res) =>
{  
    res.sendFile('public/home.html', { root: '.' })
} 
exports.form = (req, res) =>
{  
    res.sendFile('public/register.html', { root: '.' })
} 

exports.approved = (req, res) =>
{  
    res.sendFile('public/approved.html', { root: '.' })
} 
exports.napproved = (req, res) =>
{  
    res.sendFile('public/napproved.html', { root: '.' })
} 



// module to handle post request on localhost:3000 when user submits the registration form
// form data is captured and sent back as a response
exports.formprocess = async(req, res) =>
{  
   console.log(req.body);
//    res.write('<h1> Registration Successfull :-) </h1>');
//    res.write('<p> Name : </h1>'+ req.body.name);
//    res.write('<p> Username : </h1>'+ req.body.username);
//    res.write('<p> Email : </h1>'+ req.body.mail);
//    res.write('<p> Contact : </h1>'+ req.body.mobile);
//    res.end();

const data = {
    
    NPPM:req.body.nppm,
    LoanStatus:req.body.ls,
    Objective:req.body.objective,
    Amount:req.body.amount,
    Guarantee:req.body.guarantor,
    Experience: req.body.experience,
    M_Status:req.body.maritalStatus,
    ExistingLoan:req.body.existingLoan,
    Age:req.body.age,
    CA_Balance:req.body.ca_balance,
    SA_Balance:req.body.sa_balance,
    PI_Balance:req.body.pi,
    WorkAB:req.body.workab,
    PhNum:req.body.phn,
    Tenure:req.body.tenure,
    prop:req.body.prop,
    JobTyp:req.body.jobType,
    HouseT:req.body.houset,
    NOE:req.body.noe,


}
console.log(data);
 const obj = await axios.post("https://mlapi-yigp.onrender.com/predict" ,JSON.stringify(data),
 {
    headers: {
    'Content-Type': 'application/json'
    }
}
).then(res => {
    return res.data
})

console.log(obj)
if(obj === "approved"){
    res.sendFile('public/approved.html', { root: '.' });

}
else{
    res.sendFile('public/napproved.html', { root: '.' })
    ;

}

}  

// res.send is equivalent to res.write + res.end. key difference is
// res.send can be called only once where as res.write can be called multiple times followed by a res.end. 
// res.end is necessary or else browser will keep on waiting for response