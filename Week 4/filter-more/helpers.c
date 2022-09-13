#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE old_image[height][width];
    for (int row = 0; row<height>; row++)
        {
            for (int col = 0; col<width>; col++)
            {
                old_image[row][col] = image[row][col];
            }
        }
        gx[3][3] = {
        {-1, 0, 1},
        {-2, 0, 2},
        {-1, 0, 1}
        }
        gy[3][3] = {
        {-1, -2, -1},
        {0, 0, 0},
        {1, 2, 1}
        }
        
        for (int row = 0; row<height>; row++)
        {
            for (int col = 0; col<width>; col++)
            {
                old_image[row][col] = image[row][col];
            }
        
        return;
        }
}
