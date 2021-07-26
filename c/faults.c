#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <pthread.h>

#define N 1e7

pthread_rwlock_t rwlock; // Read-Write lock

void *reader(void *i) {
	int *a = (int*)i;
	while (1) {
		for (long long i = 0; i < N; ++i) {
			long long index = i * rand() % (long long)N;
			pthread_rwlock_rdlock(&rwlock);
			int x = a[index];
			pthread_rwlock_unlock(&rwlock);
		}
	}
}


void *writer(void *i) {
	int *a = (int*)i;
	while (1) {
		for (long long i = 0; i < N; ++i) {
			long long index = i * rand() % (long long)N;
			pthread_rwlock_wrlock(&rwlock);
			a[index] = 1;
			pthread_rwlock_unlock(&rwlock);
		}
	}
}


int main() {
	// Large array that exceeds the DRAM.
	int *a = malloc(N * sizeof(int));

	if (pthread_rwlock_init(&rwlock, NULL)!= 0) {
		fprintf(stderr, "Error initializing rwlock");
		return -1;
	}

	// Perform access over the array
	pthread_t threads[2];
	pthread_create(&threads[0], NULL, reader, (void*)a);
	pthread_create(&threads[1], NULL, writer, (void*)a);

	for (int i = 0; i < 2; ++i) pthread_join(threads[i], NULL);
	pthread_rwlock_destroy(&rwlock);

	free(a);
	return 0;
}

