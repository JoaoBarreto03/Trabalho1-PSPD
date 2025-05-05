package main

import (
	"context"
	"log"
	"net"
	"strings"

	pb "vm3/wordcountpb"

	"google.golang.org/grpc"
)

type server struct {
	pb.UnimplementedWordCountServiceServer
}

func (s *server) MostFrequentWord(ctx context.Context, req *pb.TextRequest) (*pb.MostFrequentWordResponse, error) {
	text := strings.ToLower(req.Text)
	words := strings.FieldsFunc(text, func(r rune) bool {
		return !('a' <= r && r <= 'z')
	})

	wordCount := make(map[string]int)
	var maxWord string
	maxCount := 0

	for _, word := range words {
		wordCount[word]++
		if wordCount[word] > maxCount {
			maxCount = wordCount[word]
			maxWord = word
		}
	}

	log.Println(text)

	return &pb.MostFrequentWordResponse{
		Word:  maxWord,
		Count: int32(maxCount),
	}, nil
}

func main() {
	lis, err := net.Listen("tcp", ":50054")
	if err != nil {
		log.Fatalf("Erro ao escutar: %v", err)
	}

	grpcServer := grpc.NewServer()
	pb.RegisterWordCountServiceServer(grpcServer, &server{})


	log.Println("Servidor gRPC escutando em :50054")
	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalf("Erro ao servir: %v", err)
	}
}
