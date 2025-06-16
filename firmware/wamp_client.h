#ifndef WAMP_CLIENT_H
#define WAMP_CLIENT_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <openssl/ssl.h>
#include <openssl/err.h>

// Mock WAMP functions for Renode testing
void wamp_connect(const char *url, const char *realm, 
                 const char *cert, const char *key) {
    printf("[WAMP] Connecting to %s...\n", url);
    sleep(1);
    printf("[WAMP] Secure connection established\n");
}

void wamp_publish(const char *topic, const char *payload) {
    printf("[WAMP] Publishing to %s: %s\n", topic, payload);
}

#endif