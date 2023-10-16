import asyncio
import logging

from InstructorEmbedding import INSTRUCTOR
from leapfrogai import (
    Embedding,
    EmbeddingRequest,
    EmbeddingResponse,
    EmbeddingsServiceServicer,
    GrpcContext,
    serve,
)

model = INSTRUCTOR("./model")


class InstructorEmbedding:
    async def CreateEmbedding(self, request: EmbeddingRequest, context: GrpcContext):
        embeddings = model.encode(request.inputs)

        embeddings = [Embedding(embedding=inner_list) for inner_list in embeddings]
        return EmbeddingResponse(embeddings=embeddings)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve(InstructorEmbedding()))