#!/usr/bin/env zx

const projectId = "2uBbvYgdqRTiiK5XbvwrKh";
const apiToken = process.env.MICROREACT_ACCESS_TOKEN;

// Get the Microreact document for the project
const resp = await fetch(
  `https://microreact.org/api/projects/json?project=${projectId}`,
  {
    headers: { "Access-Token": apiToken }
  }
);
const mrDocument = await resp.json();

// Display list of keys in the Microreact document
console.log(Object.keys(mrDocument));

// Read the content of the new metadata file 
const newMetadatafileContent = `
id,__latitude,__longitude,Country,Country__colour,Country__shape,Pedalism
Bovine,46.227638,2.213749,France,Red,Square,Four
Gibbon,15.870032,100.992541,thailand,Green,circle,Two
Orangutan,-0.589724,101.3431058,sumatra,Blue,Circle,Two
Gorilla,1.373333,32.290275,Uganda,#CC33FF,Circle,Two
Chimp,-0.228021,15.827659,Congo,orange,Circle,Two
Human,55.378051,-3.435973,UK,#CCFF33,Circle,Two
Mouse,40.463667,-3.74922,Spain,#00FFFF,square,four
NEW SAMPLE,0,0,US,#000000,,
`;
// Update metadata file
mrDocument["files"]["data-file-1"]["url"] = undefined;
mrDocument["files"]["data-file-1"]["blob"] = newMetadatafileContent;

// Update project title
mrDocument["meta"]["name"] = `Last updated at ${new Date().toISOString()}`;

// Do more updates (e.g. update tree files)

// Now we are ready to update the project
await fetch(
  `https://microreact.org/api/projects/update?project=${projectId}`,
  {
    method: "POST",
    headers: {
      "Access-Token": apiToken,
      "Content-type": "application/json; charset=UTF-8",
    },
    body: JSON.stringify(mrDocument),
  }
);
