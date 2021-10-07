/* EXETER PROGRAMMING CHALLENGE 2 - by
Name : G Mugunthan Raju
Email : mugunthanraju2000@gmail.com
*/


// Require the framework and instantiate it
const fastify = require('fastify')({ logger: true });


// JSON Data Storage
var students = new Map();


// Declared a route
fastify.get('/', (req, reply) => {
reply.send("Server working, so ready to do tasks.");
});


// This endpoint is used to add new records to the students object. Parameters to be passed will
// be a key/value pair.
fastify.post('/add', (req, reply) => {
if (students[req.body.studentID] != undefined)
reply.send(`Here, ${request.body.studentName} details exists in system.`);
students[req.body.studentID] = req.body;
reply.send(`${request.body.studentName} details added in system.`);
});


// This endpoint is used to update the mark of a particular student. Parameters to be passed will
// be a key/value pair.
fastify.post('/update', (req, reply) => {
if (students[req.body.studentID] != undefined) {
for (let key in req.body) {
students[req.body.studentID][key] = req.body[key];
} reply.send(`${request.body.studentName} mark is/are updated in the system.`);
} reply.send("Cannot find the student detail in the system.");
});


// This endpoint is used to delete the details of a student. Parameters to be passed will be a
// key/value pair.
fastify.delete('/delete', (req, reply) => {
if (students[req.body.studentID] != undefined){
delete students[req.body.studentID];
reply.send(`${request.body.studentName} details exists in system.`);
} return "Cannot find the student detail for the given ID in the system.";
});


// This endpoint is used to get a report for all the students. This does not take any parameter.
fastify.get('/report', (req, reply) => {
reply.send(students);
});


// Run the server!
const PORT = 5000
var start = async () => {
try {
await fastify.listen(PORT)
} catch (error) {
fastify.log.error(error)
process.exit(1)
}
}
start();