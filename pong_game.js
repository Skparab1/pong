// Shubham Parab     Free write program

// Pong game: this program is basically a playable pong game. its a little glichy sometimes, but otherwise it works fine.
// it also has randomised ball bouncing and speed, and a scoreboard.

function setup() {
  createCanvas(2000,800);
}

var player_scores = [0,0];

var ball_x = 1000;
var ball_y = 500;

var ball_speed = 7;

var ball_direction = 'right';
var paddlepos = 500;

function animate_ball(){
  if (ball_direction == 'right'){
    ball_x = ball_x + ball_speed;
  } else if (ball_direction == 'rightup'){
    ball_x = ball_x + ball_speed;
    ball_y = ball_y - 7;
  } else if (ball_direction == 'rightdown'){
    ball_x = ball_x + ball_speed;
    ball_y = ball_y + 7;
  } else if (ball_direction == 'left'){
    ball_x = ball_x - ball_speed;
  } else if (ball_direction == 'leftup'){
    ball_x = ball_x - ball_speed;
    ball_y = ball_y - 7;
  } else if (ball_direction == 'leftdown'){
    ball_x = ball_x - ball_speed;
    ball_y = ball_y + 7;
  }
  
  if (ball_y >= 770 && ball_direction == 'leftdown'){
    ball_direction = 'leftup';
  } else if (ball_y >= 770 && ball_direction == 'rightdown'){
    ball_direction = 'rightup';
  } else if (ball_y <= 50 && ball_direction == 'leftup'){
    ball_direction = 'leftdown';
  } else if (ball_y <= 50 && ball_direction == 'rightup'){
    ball_direction = 'rightdown';
  }
  
  if (ball_x <= 130){
    random_direction = Math.floor(Math.random() * 10);
    if (random_direction <= 4){
       ball_direction = 'rightdown';
    } else if (random_direction == 5) {
       ball_direction = 'right';
    } else {
       ball_direction = 'rightup';
    }
    ball_speed = Math.floor(Math.random() * 12) + 7;
  }  
  
  if (ball_x >= 1885){
    if (ball_y <= paddlepos+100 && ball_y >= paddlepos-100){
        random_direction = Math.floor(Math.random() * 10);
        if (random_direction <= 4){
           ball_direction = 'leftdown';
        } else if (random_direction == 5) {
           ball_direction = 'left';
        } else {
           ball_direction = 'leftup';
        }
        
        player_scores = [player_scores[0] + 1,player_scores[1]];
        for (i = 1; i <= 10; i ++){
          text('YOU MISSED!!!!!',930 + i*10,400);
        
        }
        
    ball_speed = Math.floor(Math.random() * 12) + 7;
    } else {
      player_scores = [player_scores[0],player_scores[1]+1];
      ball_x = 1000;
      ball_y = 500;
      ball_speed = 7;
      ball_direction = 'right';
     
    }
  }
}
  

function draw() {
  
  clear();
  
  line(20,20,1980,20);
  line(1980,20,1980,780);
  line(1980,780,20,780);
  line(20,780,20,20);
  line(990,20,990,780);
  
  print(ball_direction);
  print(ball_y);
  print(ball_speed);
  
  if (keyIsDown(DOWN_ARROW)) {
    paddlepos += 5;
  }

  if (keyIsDown(UP_ARROW)) {
    paddlepos -= 5;
  }
  
  to_print = 'Hits: ' + player_scores[0] + '       Misses: ' + player_scores[1] + '       Score: ' + (player_scores[0]-player_scores[1]);
  textSize(35);
  
  text(to_print,990,100);
  
  fill(50,50,50);
  rect(1900,paddlepos-100,15,200);
  rect(100,ball_y-100,15,200);
  ellipse(ball_x,ball_y,50,50);
  setTimeout(animate_ball, 1000);
}

function mouseMoved(){
  paddlepos = mouseY;
}
