int ik = 0;
boolean forwards = true;
int[] grid = init_grid();
int[] grid_original = init_grid();

void setup() {
  size(500, 500);
  background(255);
  int grid_space = draw_grid();
  int[] grid = init_grid();
  color black = color(0, 0, 0);
  text_on_grid(grid, grid_space, black);
  frameRate(4);
}

int draw_grid() {
  int border = 25;
  int grid_space = 50;
  strokeWeight(1);
  for (int i = 0; i < width; i = i+grid_space) {
    line(border, border+i, width-border, border+i);
    line(border+i, border, border+i, height-border);
  }
  strokeWeight(3);
  for (int i = 0; i < width; i = i+(grid_space*3)) {
    line(border, border+i, width-border, border+i);
    line(border+i, border, border+i, height-border);
  }
  return(grid_space);
}

void text_on_grid(int[] grid, int grid_space, color text_color) {
  textSize(32);
  fill(text_color);
  for (int i = 0; i < grid.length; i = i+1){
    if (grid[i] != 0) {
      text(str(grid[i]), (i%9)*grid_space+40, (i/9)*grid_space+62);
    }
  }
} 

int[] init_grid() {
  int[] grid = {
    6, 0, 0, 0, 0, 0, 0, 5, 1,
    0, 0, 0, 3, 0, 0, 9, 0, 8,
    0, 0, 8, 0, 0, 0, 0, 0, 3, 
    0, 4, 0, 7, 0, 0, 5, 0, 6, 
    0, 0, 0, 0, 9, 0, 8, 0, 2, 
    0, 0, 1, 8, 5, 0, 0, 3, 7, 
    5, 0, 2, 6, 0 ,0, 0, 0, 4, 
    3, 0, 0, 0, 0, 7, 0, 2, 9, 
    1, 7, 4, 9, 3, 2, 6, 8, 5
  };
  return(grid);
}

int[] cell(int ref, int[] grid){
  int cell_row = (ref/9)/3;
  int cell_column = (ref%9)/3;
  int[] cell = new int[9];
  for (int x = 0; x < 3; x = x+1){
    for (int y = 0; y < 3; y = y+1){
      cell[x+(y*3)] = grid[(cell_column*3)+(cell_row*9*3)+x+(9*y)];
    }
  }
  return(cell);
}

int[] row(int ref, int[] grid){
  int row_n = (ref/9);
  int[] row = new int[9];
  for (int x = 0; x < 9; x = x+1){
    row[x] = grid[x+(9*row_n)];
  }
  return(row);
}

int[] column(int ref, int[] grid){
  int column_n = (ref%9);
  int[] column = new int[9];
  for (int x = 0; x < 9; x = x+1){
    column[x] = grid[(x*9)+column_n];
  }
  return(column);
}

boolean is_in(int value, int[] array) {
  for (int i = 0; i < array.length; i = i+1) {
    if (value == array[i]){
      return(true);
    }
  }
  return(false);
}

void draw() {
  color blu = color(50, 50, 255);
  background(255);
  int grid_space = draw_grid();
  text_on_grid(grid, grid_space, blu);
  text_on_grid(grid_original, grid_space, 0); 
  saveFrame("frames/####.png");
  
  if ((grid_original[ik] == 0) && (forwards)) {
    for (int a = 1; a < 10; a = a+1) {
      if (!is_in(a, cell(ik, grid)) && !is_in(a, row(ik, grid)) && !is_in(a, column(ik, grid))){
        grid[ik] = a;
        ik += 1;
        break;
      }
      else {
        if (a == 9){
          forwards = false;
          ik -= 1;
          break;
        }
      }
    }
  }
  
  else if ((grid_original[ik] != 0) && (forwards)){
    ik += 1;
  }
  
  else if ((grid_original[ik] == 0) && (!forwards)){
    if (grid[ik] == 9){
      grid[ik] = 0;
      ik -= 1;
    }
    else {
      for (int a = grid[ik]+1; a < 10; a += 1){
        if (!is_in(a, cell(ik, grid)) && !is_in(a, row(ik, grid)) && !is_in(a, column(ik, grid))){
          grid[ik] = a;
          forwards = true;
          ik += 1;
          break;
        }
        else {
          if (a == 9){
            grid[ik] = 0;
            ik -= 1;
            break;
          }
        }
      }
    }
  }
  
  else if ((grid_original[ik] != 0) && (!forwards)){
    ik -= 1;
  }
  
  if (ik >= 9*9){
    printArray(grid);
    noLoop();
  }
}