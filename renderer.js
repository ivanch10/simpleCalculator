const zerorpc = require("zerorpc")
let client = new zerorpc.Client()

client.connect("tcp://127.0.0.1:4242")

client.invoke("echo", "server ready", (error, res) => {
  if(error || res !== 'server ready') {
    console.error(error)
  } else {
    console.log("server is ready")
  }
})

let numA = document.querySelector('#numA')
let numB = document.querySelector('#numB')
let submitAB = document.querySelector('#submitAB')
let sumAB = document.querySelector('#sumAB')

submitAB.addEventListener('click', () => {
  client.invoke("sum2nums", numA.value, numB.value, (error, res) => {
    console.log("invoke sum2nums");
    if(error) {
      console.error(error)
    } else {
      sumAB.value = res
    }
  })
})

// dispatch click event to caculate the demo output
submitAB.dispatchEvent(new Event('click'))
