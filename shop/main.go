package main

import (
    "github.com/gin-gonic/gin"
)

func main() {
    r := gin.Default()

    r.GET("/", func(c *gin.Context) {
        c.JSON(200, gin.H{
            "success": true,
            "message": "Shop service 1.0.3",
        })
    })

    r.Run(":4000")
} 