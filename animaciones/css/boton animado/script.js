const confettiCount = 20
const sequinCount = 10

// "physics" variables
const gravityConfetti = 0.3
const gravitySequins = 0.55
const dragConfetti = 0.075
const dragSequins = 0.02
const terminalVelocity = 3

// init other global elements
const button = document.getElementById('button')
var disabled = false
const canvas = document.getElementById('canvas')
const ctx = canvas.getContext('2d')
canvas.width = window.innerWidth
canvas.height = window.innerHeight
let cx = ctx.canvas.width / 2
let cy = ctx.canvas.height / 2

let confetti = []
let sequins = []

const colors = [
  { front: '#E0AD0B', back: '#E0AD0B' }, 
  { front: '#E0AD0B', back: '#E0AD0B' }, 
  { front: '#E0AD0B', back: '#E0AD0B' },
]

randomRange = (min, max) => Math.random() * (max - min) + min

initConfettoVelocity = (xRange, yRange) => {
  const x = randomRange(xRange[0], xRange[1])
  const range = yRange[1] - yRange[0] + 1
  let y = yRange[0] + Math.abs(randomRange(0, range) + randomRange(0, range) - range)
  if (y >= yRange[1] - 1) {
    // Occasional confetto goes higher than the max
    y -= (Math.random() < .25) ? randomRange(1, 3) : 0
  }
  return { x: x, y: -y }
}


function Confetto() {
  this.randomModifier = randomRange(0, 99)
  this.color = colors[Math.floor(randomRange(0, colors.length))]
  this.dimensions = {
    x: randomRange(5, 9),
    y: randomRange(8, 15),
  }
  this.position = {
    x: randomRange(canvas.width / 2 - button.offsetWidth / 4, canvas.width / 2 + button.offsetWidth / 4),
    y: randomRange(canvas.height / 2 + button.offsetHeight / 2, canvas.height / 2 + (1.5 * button.offsetHeight)),
  }
  this.rotation = randomRange(0, 2 * Math.PI)
  this.scale = {
    x: 1,
    y: 1,
  }
  this.velocity = initConfettoVelocity([-9, 9], [6, 11])
}

// Sequin Class
function Sequin() {
  this.color = colors[Math.floor(randomRange(0, colors.length))].back,
    this.radius = randomRange(1, 2),
    this.position = {
      x: randomRange(canvas.width / 2 - button.offsetWidth / 3, canvas.width / 2 + button.offsetWidth / 3),
      y: randomRange(canvas.height / 2 + button.offsetHeight / 2, canvas.height / 2 + (1.5 * button.offsetHeight)),
    },
    this.velocity = {
      x: randomRange(-6, 6),
      y: randomRange(-8, -12)
    }
}

Sequin.prototype.update = function () {
  // apply forces to velocity
  this.velocity.x -= this.velocity.x * dragSequins
  this.velocity.y = this.velocity.y + gravitySequins

  // set position
  this.position.x += this.velocity.x
  this.position.y += this.velocity.y
}

// add elements to arrays to be drawn
initBurst = () => {
  for (let i = 0; i < confettiCount; i++) {
    confetti.push(new Confetto())
  }
  for (let i = 0; i < sequinCount; i++) {
    sequins.push(new Sequin())
  }
}

// draws the elements on the canvas
render = () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height)

  confetti.forEach((confetto, index) => {
    let width = (confetto.dimensions.x * confetto.scale.x)
    let height = (confetto.dimensions.y * confetto.scale.y)

    // move canvas to position and rotate
    ctx.translate(confetto.position.x, confetto.position.y)
    ctx.rotate(confetto.rotation)

    // update confetto "physics" values
    confetto.update()

    // get front or back fill color
    ctx.fillStyle = confetto.scale.y > 0 ? confetto.color.front : confetto.color.back

    // draw confetto
    ctx.fillRect(-width / 2, -height / 2, width, height)

    // reset transform matrix
    ctx.setTransform(1, 0, 0, 1, 0, 0)

    // clear rectangle where button cuts off
    if (confetto.velocity.y < 0) {
      ctx.clearRect(canvas.width / 2 - button.offsetWidth / 2, canvas.height / 2 + button.offsetHeight / 2, button.offsetWidth, button.offsetHeight)
    }
  })

  sequins.forEach((sequin, index) => {
    // move canvas to position
    ctx.translate(sequin.position.x, sequin.position.y)

    // update sequin "physics" values
    sequin.update()

    // set the color
    ctx.fillStyle = sequin.color

    // draw sequin
    ctx.beginPath()
    ctx.arc(0, 0, sequin.radius, 0, 2 * Math.PI)
    ctx.fill()

    // reset transform matrix
    ctx.setTransform(1, 0, 0, 1, 0, 0)

    // clear rectangle where button cuts off
    if (sequin.velocity.y < 0) {
      ctx.clearRect(canvas.width / 2 - button.offsetWidth / 2, canvas.height / 2 + button.offsetHeight / 2, button.offsetWidth, button.offsetHeight)
    }
  })

  // remove confetti and sequins that fall off the screen
  // must be done in separate loops to avoid noticeable flickering
  confetti.forEach((confetto, index) => {
    if (confetto.position.y >= canvas.height) confetti.splice(index, 1)
  })
  sequins.forEach((sequin, index) => {
    if (sequin.position.y >= canvas.height) sequins.splice(index, 1)
  })

  window.requestAnimationFrame(render)
}

redirectToLinkInNewTab = () => {
  window.open("https://web.whatsapp.com/", "_blank");
}

// Modifica la función clickButton
clickButton = () => {
  if (!disabled) {
    disabled = true;

    // Inicia el efecto de confeti
    window.initBurst();

    // Espera a que termine la animación de confeti antes de redirigir en otra pestaña
    playConfettiAnimation().then(() => {
      // Redirecciona al enlace en otra pestaña después de que termine la animación
      redirectToLinkInNewTab();

      // Reset button so user can select it again
      disabled = false;
      button.classList.remove('complete');
      button.classList.add('ready');
    });
  }
}

// Función para animar el confeti y resolver una promesa cuando termine
playConfettiAnimation = () => {
  return new Promise((resolve) => {
    button.classList.add('complete');
    setTimeout(() => {
      window.initBurst();
      setTimeout(() => {
        // Resuelve la promesa cuando termine la animación de confeti
        resolve();
      }, 1000);
    }, 100);
  });
}

// re-init canvas if the window size changes
resizeCanvas = () => {
  canvas.width = window.innerWidth
  canvas.height = window.innerHeight
  cx = ctx.canvas.width / 2
  cy = ctx.canvas.height / 2
}

// resize listener
window.addEventListener('resize', () => {
  resizeCanvas()
})

// click button on spacebar or return keypress
document.body.onkeyup = (e) => {
  if (e.keyCode == 13 || e.keyCode == 32) {
    clickButton()
  }
}

// Set up button text transition timings on page load
textElements = button.querySelectorAll('.button-text')
textElements.forEach((element) => {
  characters = element.innerText.split('')
  let characterHTML = ''
  characters.forEach((letter, index) => {
    characterHTML += `<span class="char${index}" style="--d:${index * 30}ms; --dr:${(characters.length - index - 1) * 30}ms;">${letter}</span>`
  })
  element.innerHTML = characterHTML
})

// kick off the render loop
window.initBurst()
render()
