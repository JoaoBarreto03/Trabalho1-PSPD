// server.go
package main

import (
	"context"
	"log"
	"net"
	"strings"

	pb "vm2/wordcountpb"

	"google.golang.org/grpc"
)

type server struct {
	pb.UnimplementedWordCountServiceServer
}

func (s *server) CountWords(ctx context.Context, req *pb.TextRequest) (*pb.WordCountResponse, error) {
	wordCounts := make(map[string]int32)
	words := strings.Fields(req.Text)

	for _, word := range words {
		wordCounts[word]++
	}

	log.Println(req.Text);

	return &pb.WordCountResponse{WordCounts: wordCounts}, nil
}

func main() {
	lis, err := net.Listen("tcp", ":50053")
	if err != nil {
		log.Fatalf("Erro ao escutar: %v", err)
	}

	s := grpc.NewServer()
	pb.RegisterWordCountServiceServer(s, &server{})

	log.Println("Servidor escutando em :50053")
	if err := s.Serve(lis); err != nil {
		log.Fatalf("Erro ao iniciar servidor: %v", err)
	}
}

