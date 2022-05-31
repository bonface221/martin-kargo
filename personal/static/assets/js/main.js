console.log("Hello world!")

const copyBtns =[...document.getElementsByClassName('copy-btn')]
console.log(copyBtns)

let previous = null

copyBtns.forEach(btn=> btn.addEventListener('click', ()=>{
  console.log('click')
  const image = btn.getAttribute('data-landImage.url')
  console.log(image)
  navigator.clipboard.writeText(image)
  btn.textContent = 'copied'

  if (previous) {
    previous.textContent = 'Copy Link'
  }
  previous = btn
  
}))